import FWCore.ParameterSet.Config as cms

def PileUpFilter(**kwargs):
  mod = cms.EDFilter('PileUpFilter',
    pileupInfoSummaryInputTag = cms.InputTag('PileupSummaryInfo'),
    minPU = cms.double(0),
    maxPU = cms.double(80),
    useTrueNumInteraction = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
