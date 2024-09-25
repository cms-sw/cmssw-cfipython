import FWCore.ParameterSet.Config as cms

def PixelTrackFilterByKinematicsProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelTrackFilterByKinematicsProducer',
    ptMin = cms.double(0.1),
    nSigmaInvPtTolerance = cms.double(0),
    tipMax = cms.double(1),
    nSigmaTipMaxTolerance = cms.double(0),
    chi2 = cms.double(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
