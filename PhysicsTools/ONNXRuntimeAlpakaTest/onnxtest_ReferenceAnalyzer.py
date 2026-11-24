import FWCore.ParameterSet.Config as cms

def onnxtest_ReferenceAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('onnxtest::ReferenceAnalyzer',
    particles = cms.required.InputTag,
    images = cms.required.InputTag,
    simpleNetModel = cms.FileInPath('PhysicsTools/ONNXRuntimeAlpakaTest/data/SimpleNet.onnx'),
    multiHeadNetModel = cms.FileInPath('PhysicsTools/ONNXRuntimeAlpakaTest/data/MultiHeadNet.onnx'),
    tinyResNetModel = cms.FileInPath('PhysicsTools/ONNXRuntimeAlpakaTest/data/TinyResNet.onnx'),
    simpleNet = cms.VInputTag(),
    multiHeadNet = cms.VInputTag(),
    tinyResNet = cms.VInputTag(),
    tolerance = cms.double(0.0001),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
