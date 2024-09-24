import FWCore.ParameterSet.Config as cms

def PileupSummaryInfoSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PileupSummaryInfoSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod