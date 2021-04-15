import FWCore.ParameterSet.Config as cms

hfShowerLibaryAnalysis = cms.EDAnalyzer('HFShowerLibraryAnalyzer',
  FileName = cms.string('HFShowerLibrary_npmt_noatt_eta4_16en_v4.root'),
  TreeEMID = cms.string('emParticles'),
  TreeHadID = cms.string('hadParticles'),
  BranchEvt = cms.string(''),
  BranchPre = cms.string(''),
  BranchPost = cms.string(''),
  Verbosity = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
