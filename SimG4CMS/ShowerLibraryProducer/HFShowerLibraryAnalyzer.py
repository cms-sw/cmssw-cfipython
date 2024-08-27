import FWCore.ParameterSet.Config as cms

def HFShowerLibraryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HFShowerLibraryAnalyzer',
    FileName = cms.string('HFShowerLibrary_10000.root'),
    TreeEMID = cms.string('emParticles'),
    TreeHadID = cms.string('hadParticles'),
    BranchEvt = cms.string(''),
    BranchPre = cms.string(''),
    BranchPost = cms.string(''),
    Verbosity = cms.bool(False),
    EventPerBin = cms.int32(10000),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
