import FWCore.ParameterSet.Config as cms

def PixelTrackFilterByKinematicsProducer(**kwargs):
  mod = cms.EDProducer('PixelTrackFilterByKinematicsProducer',
    ptMin = cms.double(0.1),
    nSigmaInvPtTolerance = cms.double(0),
    tipMax = cms.double(1),
    nSigmaTipMaxTolerance = cms.double(0),
    chi2 = cms.double(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
