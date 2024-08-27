import FWCore.ParameterSet.Config as cms

def BeamSpotCompatibilityChecker(**kwargs):
  mod = cms.EDAnalyzer('BeamSpotCompatibilityChecker',
    warningThr = cms.double(1),
    errorThr = cms.double(3),
    verbose = cms.untracked.bool(False),
    bsFromEvent = cms.InputTag(''),
    dbFromEvent = cms.bool(False),
    bsFromDB = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
