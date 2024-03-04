import FWCore.ParameterSet.Config as cms

def GTTFileReader(**kwargs):
  mod = cms.EDProducer('GTTFileReader',
    files = cms.vstring('gttOutput_0.txt'),
    format = cms.untracked.string('APx'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
