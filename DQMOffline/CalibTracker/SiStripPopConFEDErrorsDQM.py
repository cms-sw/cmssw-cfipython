import FWCore.ParameterSet.Config as cms

def SiStripPopConFEDErrorsDQM(**kwargs):
  mod = cms.EDProducer('SiStripPopConFEDErrorsDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
