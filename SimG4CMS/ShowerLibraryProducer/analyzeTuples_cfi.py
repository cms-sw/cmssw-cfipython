import FWCore.ParameterSet.Config as cms

analyzeTuples = cms.EDAnalyzer('AnalyzeTuples',
  FileName = cms.string('SimG4CMS/Calo/data/HFShowerLibrary_oldpmt_noatt_eta4_16en_v3.root'),
  TreeEMID = cms.string('emParticles'),
  TreeHadID = cms.string('hadParticles'),
  BranchEvt = cms.string(''),
  BranchPre = cms.string(''),
  BranchPost = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)