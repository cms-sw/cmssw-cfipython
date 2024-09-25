import FWCore.ParameterSet.Config as cms

def PixelDCSObjectReader_PixelCaenChannelRcd_(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelDCSObjectReader<PixelCaenChannelRcd>',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
