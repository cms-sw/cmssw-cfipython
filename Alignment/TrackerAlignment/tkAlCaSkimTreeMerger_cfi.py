import FWCore.ParameterSet.Config as cms

tkAlCaSkimTreeMerger = cms.EDAnalyzer('TkAlCaSkimTreeMerger',
  FileList = cms.string('DQMHitMapsList.txt'),
  TreeName = cms.string('AlignmentHitMaps'),
  OutputFile = cms.string('AlignmentHitMapsMerged.root'),
  NhitsMaxLimit = cms.int32(0),
  NhitsMaxSet = cms.VPSet(
    cms.PSet(
      PXBmaxhits = cms.int32(-1),
      PXFmaxhits = cms.int32(-1),
      TECmaxhits = cms.int32(-1),
      TIBmaxhits = cms.int32(-1),
      TIDmaxhits = cms.int32(-1),
      TOBmaxhits = cms.int32(-1)
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
