import FWCore.ParameterSet.Config as cms

beamSpotAnalyzer = cms.EDAnalyzer('BeamSpotAnalyzer',
  BSAnalyzerParameters = cms.VPSet(
    cms.PSet(
      RunAllFitters = cms.bool(False),
      RunBeamWidthFit = cms.bool(False),
      WriteToDB = cms.bool(False),
      fitEveryNLumi = cms.untracked.int32(-1),
      resetEveryNLumi = cms.untracked.int32(-1)
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
