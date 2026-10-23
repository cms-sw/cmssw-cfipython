import FWCore.ParameterSet.Config as cms

def SiStripSpyEventSummaryProducer(*args, **kwargs):
  mod = cms.EDProducer('SiStripSpyEventSummaryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
