import FWCore.ParameterSet.Config as cms

def L1TrackVertexAssociationProducer(**kwargs):
  mod = cms.EDProducer('L1TrackVertexAssociationProducer',
    l1TracksInputTag = cms.InputTag('l1tGTTInputProducer', 'Level1TTTracksConverted'),
    l1SelectedTracksInputTag = cms.InputTag('l1tTrackSelectionProducer', 'Level1TTTracksSelected'),
    l1SelectedTracksEmulationInputTag = cms.InputTag('l1tTrackSelectionProducer', 'Level1TTTracksSelectedEmulation'),
    l1VerticesInputTag = cms.InputTag('l1tVertexFinder', 'L1Vertices'),
    l1VerticesEmulationInputTag = cms.InputTag('l1tVertexFinderEmulator', 'L1VerticesEmulation'),
    outputCollectionName = cms.string('Level1TTTracksSelectedAssociated'),
    cutSet = cms.PSet(
      deltaZMaxEtaBounds = cms.vdouble(
        0,
        0.7,
        1,
        1.2,
        1.6,
        2,
        2.4
      ),
      deltaZMax = cms.vdouble(
        0.37,
        0.5,
        0.6,
        0.75,
        1,
        1.6
      )
    ),
    useDisplacedTracksDeltaZOverride = cms.double(-1),
    processSimulatedTracks = cms.bool(True),
    processEmulatedTracks = cms.bool(True),
    fwNTrackSetsTVA = cms.uint32(94),
    debug = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
