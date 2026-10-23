import FWCore.ParameterSet.Config as cms

def SiPixelPhase1ResidualsExtra(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1ResidualsExtra',
    TopFolderName = cms.string('PixelPhase1/Tracks/ResidualsExtra'),
    InputFolderName = cms.string(''),
    MinHits = cms.int32(30),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
