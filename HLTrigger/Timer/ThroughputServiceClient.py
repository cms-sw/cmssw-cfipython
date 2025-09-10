import FWCore.ParameterSet.Config as cms

def ThroughputServiceClient(*args, **kwargs):
  mod = cms.EDProducer('ThroughputServiceClient',
    dqmPath = cms.untracked.string('HLT/Throughput'),
    createSummary = cms.untracked.bool(True),
    fillEveryLumiSection = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
