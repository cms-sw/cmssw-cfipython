import FWCore.ParameterSet.Config as cms

def TriggerRatesMonitorClient(**kwargs):
  mod = cms.EDProducer('TriggerRatesMonitorClient',
    dqmPath = cms.untracked.string('HLT/Datasets'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
