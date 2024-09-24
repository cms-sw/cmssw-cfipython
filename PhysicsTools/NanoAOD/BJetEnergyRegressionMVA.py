import FWCore.ParameterSet.Config as cms

def BJetEnergyRegressionMVA(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
