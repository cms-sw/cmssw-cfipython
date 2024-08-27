import FWCore.ParameterSet.Config as cms

def ThroughputServiceClient(**kwargs):
  mod = cms.EDProducer('ThroughputServiceClient',
    dqmPath = cms.untracked.string('HLT/Throughput'),
    createSummary = cms.untracked.bool(True),
    fillEveryLumiSection = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
