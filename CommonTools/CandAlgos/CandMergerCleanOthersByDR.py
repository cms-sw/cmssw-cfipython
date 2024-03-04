import FWCore.ParameterSet.Config as cms

def CandMergerCleanOthersByDR(**kwargs):
  mod = cms.EDProducer('CandMergerCleanOthersByDR',
    coll1 = cms.InputTag('egammasForCoreTracking'),
    coll2 = cms.InputTag('jetsForCoreTracking'),
    maxDRToClean = cms.double(0.05),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
