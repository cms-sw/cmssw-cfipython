import FWCore.ParameterSet.Config as cms

def CTPPSDiamondDQMSource(*args, **kwargs):
  mod = cms.EDProducer('CTPPSDiamondDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
