import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromLegacyPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromLegacyPhase1',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    CPE = cms.string('PixelCPEFast'),
    convertToLegacy = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
