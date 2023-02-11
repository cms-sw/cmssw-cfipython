import FWCore.ParameterSet.Config as cms

hltppsJetComparisonFilter = cms.EDFilter('HLTPPSJetComparisonFilter',
  jetInputTag = cms.InputTag('hltAK4PFJetsCorrected'),
  forwardProtonInputTag = cms.InputTag('ctppsProtons', 'singleRP'),
  lhcInfoLabel = cms.string(''),
  maxDiffxi = cms.double(1),
  maxDiffm = cms.double(1),
  maxDiffy = cms.double(1),
  nJets = cms.uint32(2),
  do_xi = cms.bool(True),
  do_my = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
