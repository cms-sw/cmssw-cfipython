import FWCore.ParameterSet.Config as cms

def SiStripSpyEventSummaryProducer(**kwargs):
  mod = cms.EDProducer('SiStripSpyEventSummaryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
