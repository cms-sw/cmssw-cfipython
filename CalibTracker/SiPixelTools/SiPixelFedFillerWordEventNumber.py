import FWCore.ParameterSet.Config as cms

def SiPixelFedFillerWordEventNumber(*args, **kwargs):
  mod = cms.EDProducer('SiPixelFedFillerWordEventNumber',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
