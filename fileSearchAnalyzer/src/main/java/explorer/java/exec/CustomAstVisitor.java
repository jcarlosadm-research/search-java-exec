package explorer.java.exec;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.jdt.core.ICompilationUnit;
import org.eclipse.jdt.core.JavaCore;
import org.eclipse.jdt.core.dom.AST;
import org.eclipse.jdt.core.dom.ASTParser;
import org.eclipse.jdt.core.dom.ASTVisitor;
import org.eclipse.jdt.core.dom.CompilationUnit;
import org.eclipse.jdt.core.dom.TypeDeclaration;

public class CustomAstVisitor extends ASTVisitor {

	boolean isClass = false;

	boolean hasImplMethods = false;

	private void startVisit(IFile file) {
		ICompilationUnit icu = JavaCore.createCompilationUnitFrom(file);

		ASTParser parser = ASTParser.newParser(AST.JLS3);
		parser.setResolveBindings(true);
		parser.setSource(icu);

		CompilationUnit cu = (CompilationUnit) parser.createAST(null);
		cu.accept(this);
	}

	@Override
	public boolean visit(TypeDeclaration node) {
		// TODO Auto-generated method stub
		System.out.println(node.getName());

		return super.visit(node);
	}

	public static void main(String[] args) {

		// File file = new File(args[0]);
		//
		// try {
		// BufferedReader bReader = new BufferedReader(new FileReader(file));
		// String line;
		// String lines = "";
		// while((line = bReader.readLine()) != null) {
		// lines += line + "\n";
		// }
		// bReader.close();
		//
		//
		// CustomAstVisitor customAstVisitor = new CustomAstVisitor();
		// new JDTRunner().visit(customAstVisitor, new
		// ByteArrayInputStream(lines.getBytes()));
		// } catch (Exception e) {
		// // TODO: handle exception
		// e.printStackTrace();
		// }

		CustomAstVisitor ast = new CustomAstVisitor();
		ast.startVisit(ResourcesPlugin.getWorkspace().getRoot().getProject("java.explorer.exec")
				.getFile("JavaParserVisitor.java"));

	}

}
