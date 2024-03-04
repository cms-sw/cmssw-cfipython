import FWCore.ParameterSet.Config as cms

def SiStripSpyUnpackerModule(**kwargs):
  mod = cms.EDProducer('SiStripSpyUnpackerModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
