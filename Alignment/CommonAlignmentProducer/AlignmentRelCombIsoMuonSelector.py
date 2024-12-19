import FWCore.ParameterSet.Config as cms

def AlignmentRelCombIsoMuonSelector(**kwargs):
  mod = cms.EDFilter('AlignmentRelCombIsoMuonSelector',
    src = cms.InputTag('muons'),
    relCombIsoCut = cms.double(0.15),
    useTrackerOnlyIsolation = cms.bool(False),
    filter = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
