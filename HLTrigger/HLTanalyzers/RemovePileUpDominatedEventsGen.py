import FWCore.ParameterSet.Config as cms

def RemovePileUpDominatedEventsGen(*args, **kwargs):
  mod = cms.EDFilter('RemovePileUpDominatedEventsGen',
    pileupSummaryInfos = cms.InputTag('addPileupInfo'),
    generatorInfo = cms.InputTag('generator'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
