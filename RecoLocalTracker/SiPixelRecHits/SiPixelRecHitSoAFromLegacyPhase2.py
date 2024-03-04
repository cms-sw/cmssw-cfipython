import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromLegacyPhase2(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromLegacyPhase2',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    CPE = cms.string('PixelCPEFastPhase2'),
    convertToLegacy = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
