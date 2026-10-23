import FWCore.ParameterSet.Config as cms

def CandMergerCleanOthersByDR(*args, **kwargs):
  mod = cms.EDProducer('CandMergerCleanOthersByDR',
    coll1 = cms.InputTag('egammasForCoreTracking'),
    coll2 = cms.InputTag('jetsForCoreTracking'),
    maxDRToClean = cms.double(0.05),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
