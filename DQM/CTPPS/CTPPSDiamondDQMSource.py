import FWCore.ParameterSet.Config as cms

def CTPPSDiamondDQMSource(**kwargs):
  mod = cms.EDProducer('CTPPSDiamondDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
