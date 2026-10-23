import FWCore.ParameterSet.Config as cms

def BPHWriteSpecificDecay(*args, **kwargs):
  mod = cms.EDProducer('BPHWriteSpecificDecay',
    pVertexLabel = cms.string(''),
    patMuonLabel = cms.string(''),
    ccCandsLabel = cms.string(''),
    pfCandsLabel = cms.string(''),
    pcCandsLabel = cms.string(''),
    gpCandsLabel = cms.string(''),
    k0CandsLabel = cms.string(''),
    l0CandsLabel = cms.string(''),
    kSCandsLabel = cms.string(''),
    lSCandsLabel = cms.string(''),
    oniaName = cms.string('oniaCand'),
    sdName = cms.string('kx0Cand'),
    ssName = cms.string('phiCand'),
    buName = cms.string('buFitted'),
    bpName = cms.string('bpFitted'),
    bdName = cms.string('bdFitted'),
    bsName = cms.string('bsFitted'),
    k0Name = cms.string('k0Fitted'),
    l0Name = cms.string('l0Fitted'),
    b0Name = cms.string('b0Fitted'),
    lbName = cms.string('lbFitted'),
    bcName = cms.string('bcFitted'),
    psi2SName = cms.string('psi2SFitted'),
    x3872Name = cms.string('x3872Fitted'),
    writeVertex = cms.bool(True),
    writeMomentum = cms.bool(True),
    recoSelect = cms.VPSet(
      template = cms.PSetTemplate(
        name = cms.required.string,
        ptMin = cms.double(-2e+35),
        etaMax = cms.double(-2e+35),
        mJPsiMin = cms.double(-2e+35),
        mJPsiMax = cms.double(-2e+35),
        mKx0Min = cms.double(-2e+35),
        mKx0Max = cms.double(-2e+35),
        mPhiMin = cms.double(-2e+35),
        mPhiMax = cms.double(-2e+35),
        mK0sMin = cms.double(-2e+35),
        mK0sMax = cms.double(-2e+35),
        mLambda0Min = cms.double(-2e+35),
        mLambda0Max = cms.double(-2e+35),
        massMin = cms.double(-2e+35),
        massMax = cms.double(-2e+35),
        probMin = cms.double(-2e+35),
        massFitMin = cms.double(-2e+35),
        massFitMax = cms.double(-2e+35),
        constrMass = cms.double(-2e+35),
        constrSigma = cms.double(-2e+35),
        requireJPsi = cms.bool(True),
        constrMJPsi = cms.bool(True),
        constrMPsi2 = cms.bool(True),
        writeCandidate = cms.bool(True)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
