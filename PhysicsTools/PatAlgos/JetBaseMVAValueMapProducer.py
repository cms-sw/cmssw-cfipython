import FWCore.ParameterSet.Config as cms

def JetBaseMVAValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('JetBaseMVAValueMapProducer',
    src = cms.required.InputTag,
    name = cms.required.string,
    weightFile = cms.required.FileInPath,
    batch_eval = cms.bool(False),
    variables = cms.required.VPSet,
    backend = cms.string('TMVA'),
    isClassifier = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
