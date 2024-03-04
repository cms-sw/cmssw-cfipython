import FWCore.ParameterSet.Config as cms

def HLTObjectMonitorProtonLead(**kwargs):
  mod = cms.EDProducer('HLTObjectMonitorProtonLead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
