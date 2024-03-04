import FWCore.ParameterSet.Config as cms

def HLTPPSJetComparisonFilter(**kwargs):
  mod = cms.EDFilter('HLTPPSJetComparisonFilter',
    jetInputTag = cms.InputTag('hltAK4PFJetsCorrected'),
    forwardProtonInputTag = cms.InputTag('ctppsProtons', 'singleRP'),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    useNewLHCInfo = cms.bool(True),
    maxDiffxi = cms.double(1),
    maxDiffm = cms.double(1),
    maxDiffy = cms.double(1),
    nJets = cms.uint32(2),
    do_xi = cms.bool(True),
    do_my = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
