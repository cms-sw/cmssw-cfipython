import FWCore.ParameterSet.Config as cms

def AlignmentRelCombIsoMuonSelector(*args, **kwargs):
  mod = cms.EDFilter('AlignmentRelCombIsoMuonSelector',
    src = cms.InputTag('muons'),
    relCombIsoCut = cms.double(0.15),
    useTrackerOnlyIsolation = cms.bool(False),
    filter = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
