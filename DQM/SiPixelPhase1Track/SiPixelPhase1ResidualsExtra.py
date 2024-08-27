import FWCore.ParameterSet.Config as cms

def SiPixelPhase1ResidualsExtra(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1ResidualsExtra',
    TopFolderName = cms.string('PixelPhase1/Tracks/ResidualsExtra'),
    InputFolderName = cms.string(''),
    MinHits = cms.int32(30),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
