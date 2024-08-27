import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromLegacyHIonPhase1(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromLegacyHIonPhase1',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    CPE = cms.string('PixelCPEFastHIonPhase1'),
    convertToLegacy = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
