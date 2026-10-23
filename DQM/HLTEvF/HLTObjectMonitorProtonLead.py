import FWCore.ParameterSet.Config as cms

def HLTObjectMonitorProtonLead(*args, **kwargs):
  mod = cms.EDProducer('HLTObjectMonitorProtonLead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
