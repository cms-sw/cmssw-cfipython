import FWCore.ParameterSet.Config as cms

def PixelDCSObjectReader_PixelCaenChannelRcd_(**kwargs):
  mod = cms.EDAnalyzer('PixelDCSObjectReader<PixelCaenChannelRcd>',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
