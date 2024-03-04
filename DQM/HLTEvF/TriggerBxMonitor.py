import FWCore.ParameterSet.Config as cms

def TriggerBxMonitor(**kwargs):
  mod = cms.EDProducer('TriggerBxMonitor',
    l1tResults = cms.untracked.InputTag('gtStage2Digis'),
    hltResults = cms.untracked.InputTag('TriggerResults'),
    dqmPath = cms.untracked.string('HLT/TriggerBx'),
    make1DPlots = cms.untracked.bool(True),
    make2DPlots = cms.untracked.bool(False),
    lsRange = cms.untracked.uint32(4000),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
