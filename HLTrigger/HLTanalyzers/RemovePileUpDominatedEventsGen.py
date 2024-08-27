import FWCore.ParameterSet.Config as cms

def RemovePileUpDominatedEventsGen(**kwargs):
  mod = cms.EDFilter('RemovePileUpDominatedEventsGen',
    pileupSummaryInfos = cms.InputTag('addPileupInfo'),
    generatorInfo = cms.InputTag('generator'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
