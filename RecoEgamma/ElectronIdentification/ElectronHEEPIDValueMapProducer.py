import FWCore.ParameterSet.Config as cms

def ElectronHEEPIDValueMapProducer(**kwargs):
  mod = cms.EDProducer('ElectronHEEPIDValueMapProducer',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    ebRecHitsAOD = cms.InputTag('reducedEcalRecHitsEB'),
    eeRecHitsAOD = cms.InputTag('reducedEcalRecHitsEE'),
    candsAOD = cms.VInputTag('packedCandidates'),
    candVetosAOD = cms.vstring('none'),
    elesAOD = cms.InputTag('gedGsfElectrons'),
    ebRecHitsMiniAOD = cms.InputTag('reducedEcalRecHitsEB'),
    eeRecHitsMiniAOD = cms.InputTag('reducedEcalRecHitsEE'),
    candsMiniAOD = cms.VInputTag('packedCandidates'),
    candVetosMiniAOD = cms.vstring('none'),
    elesMiniAOD = cms.InputTag('gedGsfElectrons'),
    dataFormat = cms.int32(0),
    makeTrkIso04 = cms.bool(False),
    trkIsoConfig = cms.PSet(
      barrelCuts = cms.PSet(
        minPt = cms.double(1),
        maxDR = cms.double(0.3),
        minDR = cms.double(0),
        minDEta = cms.double(0.005),
        maxDZ = cms.double(0.1),
        maxDPtPt = cms.double(-1),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        allowedQualities = cms.required.vstring,
        algosToReject = cms.required.vstring
      ),
      endcapCuts = cms.PSet(
        minPt = cms.double(1),
        maxDR = cms.double(0.3),
        minDR = cms.double(0),
        minDEta = cms.double(0.005),
        maxDZ = cms.double(0.1),
        maxDPtPt = cms.double(-1),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        allowedQualities = cms.required.vstring,
        algosToReject = cms.required.vstring
      )
    ),
    trkIso04Config = cms.PSet(
      barrelCuts = cms.PSet(
        minPt = cms.double(1),
        maxDR = cms.double(0.3),
        minDR = cms.double(0),
        minDEta = cms.double(0.005),
        maxDZ = cms.double(0.1),
        maxDPtPt = cms.double(-1),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        allowedQualities = cms.required.vstring,
        algosToReject = cms.required.vstring
      ),
      endcapCuts = cms.PSet(
        minPt = cms.double(1),
        maxDR = cms.double(0.3),
        minDR = cms.double(0),
        minDEta = cms.double(0.005),
        maxDZ = cms.double(0.1),
        maxDPtPt = cms.double(-1),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        allowedQualities = cms.required.vstring,
        algosToReject = cms.required.vstring
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
