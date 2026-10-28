import FWCore.ParameterSet.Config as cms

def TruthGraphSummaryValidator(*args, **kwargs):
  mod = cms.EDProducer('TruthGraphSummaryValidator',
    src = cms.InputTag('truthLogicalGraphProducer'),
    folder = cms.string('TruthInfo/Graph'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
