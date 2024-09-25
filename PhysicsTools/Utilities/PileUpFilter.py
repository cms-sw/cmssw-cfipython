import FWCore.ParameterSet.Config as cms

def PileUpFilter(*args, **kwargs):
  mod = cms.EDFilter('PileUpFilter',
    pileupInfoSummaryInputTag = cms.InputTag('PileupSummaryInfo'),
    minPU = cms.double(0),
    maxPU = cms.double(80),
    useTrueNumInteraction = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
