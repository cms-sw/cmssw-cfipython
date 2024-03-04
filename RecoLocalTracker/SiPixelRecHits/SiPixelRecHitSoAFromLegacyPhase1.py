import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromLegacyPhase1(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromLegacyPhase1',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    CPE = cms.string('PixelCPEFast'),
    convertToLegacy = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
