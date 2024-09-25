import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromLegacyHIonPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromLegacyHIonPhase1',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    CPE = cms.string('PixelCPEFastHIonPhase1'),
    convertToLegacy = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
