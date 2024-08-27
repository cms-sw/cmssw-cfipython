import FWCore.ParameterSet.Config as cms

def BJetEnergyRegressionMVA(**kwargs):
  mod = cms.EDProducer('BJetEnergyRegressionMVA',
    src = cms.required.InputTag,
    name = cms.required.string,
    weightFile = cms.required.FileInPath,
    batch_eval = cms.bool(False),
    variables = cms.required.VPSet,
    backend = cms.string('TMVA'),
    isClassifier = cms.bool(True),
    pvsrc = cms.required.InputTag,
    svsrc = cms.required.InputTag,
    rhosrc = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
