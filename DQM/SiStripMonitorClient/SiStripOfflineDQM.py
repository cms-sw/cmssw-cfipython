import FWCore.ParameterSet.Config as cms

def SiStripOfflineDQM(**kwargs):
  mod = cms.EDProducer('SiStripOfflineDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
