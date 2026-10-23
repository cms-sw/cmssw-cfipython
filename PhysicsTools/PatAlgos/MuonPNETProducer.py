import FWCore.ParameterSet.Config as cms

def MuonPNETProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonPNETProducer',
    src = cms.required.InputTag,
    srcLeps = cms.required.InputTag,
    flav_names = cms.required.vstring,
    preprocess_json = cms.string('PhysicsTools/NanoAOD/data/PNetMuonId/preprocess.json'),
    model_path = cms.FileInPath('PhysicsTools/NanoAOD/data/PNetMuonId/model.onnx'),
    debugMode = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
