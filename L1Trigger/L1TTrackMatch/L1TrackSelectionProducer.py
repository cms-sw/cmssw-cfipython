import FWCore.ParameterSet.Config as cms

def L1TrackSelectionProducer(**kwargs):
  mod = cms.EDProducer('L1TrackSelectionProducer',
    l1TracksInputTag = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
    outputCollectionName = cms.string('Level1TTTracksSelected'),
    cutSet = cms.PSet(
      ptMin = cms.double(2),
      absEtaMax = cms.double(2.4),
      absZ0Max = cms.double(15),
      nStubsMin = cms.int32(4),
      nPSStubsMin = cms.int32(0),
      promptMVAMin = cms.double(-1),
      reducedBendChi2Max = cms.double(2.25),
      reducedChi2RZMax = cms.double(5),
      reducedChi2RPhiMax = cms.double(20),
      reducedChi2RZMaxNstub4 = cms.double(999.9),
      reducedChi2RZMaxNstub5 = cms.double(999.9),
      reducedChi2RPhiMaxNstub4 = cms.double(999.9),
      reducedChi2RPhiMaxNstub5 = cms.double(999.9),
      reducedBendChi2MaxNstub4 = cms.double(999.9),
      reducedBendChi2MaxNstub5 = cms.double(999.9)
    ),
    processSimulatedTracks = cms.bool(True),
    processEmulatedTracks = cms.bool(True),
    debug = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod